//Keeping track of how many rows there are
document.rowNumber = 1;

//Inserts a new value line
$('#insert-line').click(insertLine);

function insertLine(){
  if (document.rowNumber < 8){
    document.rowNumber += 1;
    item = $('tr:nth-child(' + document.rowNumber + ')');
    item.css('visibility', 'visible');
    item.find('input').prop('required', true);
    updateTotal();
  }else {
    $('#error_message').text('Maximum of 8 values')
  }
}

//Removes a value line
$('#remove-line').click(function(){
  if (document.rowNumber > 1){
    item = $('tr:nth-child(' + document.rowNumber + ')');
    item.find('input').prop('required', false);
    item.css('visibility', 'collapse');
    document.rowNumber -= 1;
    $('#error_message').text('');
    updateTotal();
  }
})

//Updates total at bottom left of screen
function updateTotal (){
  inputVal = $('.input-val');
  inputQty = $('.input-qty');
  var totalAmount = 0;

  for (var i = 0; i < document.rowNumber; i++) {
    if (inputVal.eq(i).val() && inputQty.eq(i).val()){
      totalAmount += (inputVal.eq(i).val() * inputQty.eq(i).val());
    }
  }
  $('#total-amount').text(formatNumber(totalAmount.toFixed(2)));
}

//Formats a number to add commas
function formatNumber(num) {
  return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
}

$('.input-val').on("input", updateTotal);
$('.input-qty').on("input" ,updateTotal);

//Check that nothing is already filled in
initList = $('.input-val');
for (var i = 1; i < 8; i++) {
  if (initList.eq(i).val()) {
    insertLine();
  }else {
    break;
  }
}
