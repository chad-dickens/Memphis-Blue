"""Module for creating gift card invoices. Contains one class for this purpose."""

from fpdf import FPDF


class GiftCardsInvoice(FPDF):
    """Class for the creation of gift cards invoices"""

    def __init__(self, my_dict, grand_total, image_name):
        """
        Calls super class immediately to create PDF.
        my_dict should be a dictionary containing form values, form quantities, order number,
        order date, the first and last name of the person who ordered the cards, the company,
        and address.
        grand_total should be a string of the total amount due with '$' at front and appropriate
        commas and decimal places.
        image_name should be the name and path of the image to be used as a logo on the invoice.
        """
        super().__init__(orientation='P', unit='mm', format='A4')
        self.my_dict = my_dict
        self.grand_total = grand_total
        self.image_name = image_name
        self.reg_font = 12
        self.reg_height = 7
        self.add_page()
        self.add_body()

    def header(self):
        """Adds document header. Is called automatically when the add_page method is called."""
        # Title and company logo
        self.ln(10)
        self.set_font('Arial', 'B', size=45)
        self.cell(w=95, h=17, txt='INVOICE', align='L', ln=1, border=0)
        self.image(name=self.image_name, x=130, y=10, h=60)

        # Company Info
        self.set_font('Arial', 'B', size=self.reg_font)
        self.cell(w=95, h=self.reg_height, txt='Sydney Roosters Pty Ltd',
                  align='L', ln=1, border=0)

        self.set_font('Arial', '')
        self.cell(w=95, h=self.reg_height, txt='Easts to Win, Roosters Way',
                  align='L', ln=1, border=0)
        self.cell(w=95, h=self.reg_height, txt='2026 NSW', align='L', ln=1, border=0)
        self.ln(self.reg_height)

        # Billing and shipping info
        self.set_font('Arial', 'B')
        self.cell(w=142.5, h=self.reg_height, txt='Billing and Shipping To:',
                  align='L', ln=1, border=0)

        self.set_font('Arial', '')
        self.cell(w=190, h=self.reg_height,
                  txt='{} {}'.format(self.my_dict['first_name'], self.my_dict['last_name']),
                  align='L', ln=1, border=0)
        self.cell(w=190, h=self.reg_height, txt=self.my_dict['company'], align='L', ln=1, border=0)
        self.cell(w=190, h=self.reg_height, txt=self.my_dict['address'], align='L', ln=1, border=0)
        self.ln(self.reg_height)

        # Order number and invoice date line
        self.set_font('Arial', 'B')
        self.cell(w=47.5, h=self.reg_height, txt='Order date:', align='L', ln=0, border=0)
        self.set_font('Arial', '')
        self.cell(w=47.5, h=self.reg_height, txt=self.my_dict['order_date'].strftime('%-d %b %Y'),
                  align='L', ln=0, border=0)
        self.set_font('Arial', 'B')
        self.cell(w=47.5, h=self.reg_height, txt='Order number:', align='L', ln=0, border=0)
        self.set_font('Arial', '')
        self.cell(w=47.5, h=self.reg_height, txt=self.my_dict['order_number'],
                  align='L', ln=1, border=0)
        self.ln(self.reg_height)

        # Adding the top of the items table
        self.set_font('Arial', 'B')
        self.cell(w=142.5, h=self.reg_height, txt='Gift Cards Ordered', align='L', ln=0, border=1)
        self.cell(w=47.5, h=self.reg_height, txt='Total', align='L', ln=1, border=1)

    def add_body(self):
        """Adds document body"""
        self.set_font('Arial', '')
        store_y = self.get_y()
        # Loops through each value and quantity set in the dictionary
        for i in range(1, 9):
            val = self.my_dict['val_{}'.format(i)]
            qty = self.my_dict['qty_{}'.format(i)]
            if val and qty:
                self.cell(w=142.5, h=self.reg_height, txt='- ${} x {:,}'.format(val, qty),
                          align='L', ln=0, border=0)
                self.cell(w=47.5, h=self.reg_height, txt='{:,}'.format(val * qty),
                          align='L', ln=1, border=0)

        # Drawing some lines
        self.line(10, store_y, 10, self.get_y())
        self.line(152.5, store_y, 152.5, self.get_y())
        self.line(200, store_y, 200, self.get_y())

    def footer(self):
        """Adds document footer. Is called automatically when the output method is called."""
        self.set_font('Arial', 'B')
        self.cell(w=142.5, h=self.reg_height, txt='Total Amount Due', align='L', ln=0, border=1)
        self.cell(w=47.5, h=self.reg_height, txt=self.grand_total, align='L', ln=1, border=1)
        self.ln(self.reg_height)

        self.cell(w=190, h=self.reg_height, txt='Please Pay Into The Following Account:',
                  align='L', ln=1, border=0)
        self.cell(w=190, h=self.reg_height, txt='BSB: 145-657', align='L', ln=1, border=0)
        self.cell(w=190, h=self.reg_height, txt='ACC: 6478 9283', align='L', ln=1, border=0)
        self.ln(self.reg_height)

        self.set_font('Arial', '')
        self.cell(w=190, h=self.reg_height,
                  txt='Once payment has been received, your order will be processed.',
                  align='L', ln=1, border=0)
        self.cell(w=190, h=self.reg_height,
                  txt='Thank you for your business.',
                  align='L', ln=1, border=0)
