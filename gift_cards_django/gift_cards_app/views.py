from django.shortcuts import render
from gift_cards_app.forms import OrderForm
from django.utils.crypto import get_random_string
from gift_cards_app.models import Orders
from gift_cards.settings import TIME_ZONE, STATIC_DIR
from datetime import datetime
import pytz
from gift_cards_app.gift_cards_invoice import GiftCardsInvoice
import os
from gift_cards_app.email_module import send_email_365

# Create your views here.

def order_form(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():

            # Adding item to database with order code
            new_object = form.save(commit=False)
            new_object.order_status = 'Ordered'

            # Creating a unique random string that does not currently exist in database
            while True:
                random_string = get_random_string(length=10)

                if not Orders.objects.filter(order_number=random_string).exists():
                    new_object.order_number = random_string
                    break

            new_object.save()

            # Retrieving all items from this new record as a dictionary for invoice creation
            order_dict = Orders.objects.filter(order_number=random_string).values()[0]

            # Changing the timezone for the dictionary to local time
            local_timezone = pytz.timezone(TIME_ZONE)
            order_dict['order_date'] = order_dict['order_date'].astimezone(local_timezone)

            # Determining the total value of order to add it onto confirmation page
            total_amount = 0
            order_list = []
            for i in range(1, 9):
                val = order_dict['val_{}'.format(i)]
                qty = order_dict['qty_{}'.format(i)]
                if val and qty:
                    total_amount += val * qty
                    order_list.append('${} x {:,}'.format(val, qty))
            total_amount = '${:,}.00'.format(total_amount)

            # Create invoice and send email
            pdf_image_name = os.path.join(STATIC_DIR, 'gift_cards_app', 'images', 'roosters.png')
            pdf_save_location = os.path.join(STATIC_DIR, 'gift_cards_app', 'pdfs',
                                             '{} {}.pdf'.format(order_dict['company'],
                                             order_dict['order_number']))

            pdf_invoice = GiftCardsInvoice(order_dict, total_amount, pdf_image_name)
            pdf_invoice.output(pdf_save_location)

            email_message = 'Hi {},\n'.format(order_dict['first_name'])
            email_message += 'Please find your invoice attached for the gift cards you ordered.\n'
            email_message += 'One we have received your payment, we\'ll send the cards through.\n'
            email_message += 'Regards - The team'

            send_email_365(email_recipient=order_dict['email'],
                           email_subject='Gift Cards {}'.format(order_dict['order_number']),
                           email_message=email_message,
                           email_sender='#####',
                           email_password='#####',
                           attachments=(pdf_save_location,))

            # Returning the confirmation page
            return confirmation(request, email_address=order_dict['email'],
                                order_number=random_string,
                                order_time=order_dict['order_date'], order_list=order_list,
                                order_total=total_amount)

    return render(request, 'gift_cards_app/order_form.html', {'form': form})

def confirmation(request, email_address, order_number, order_time, order_list, order_total):
    my_dict = {'customer_email': email_address, 'customer_order': order_number,
               'order_time': order_time, 'order_list': order_list, 'order_total': order_total}

    return render(request, 'gift_cards_app/confirmation.html', context=my_dict)
