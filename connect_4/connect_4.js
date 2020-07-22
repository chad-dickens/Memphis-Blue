//Keeping track of who's turn it is
document.playerTurn = 'Red';
//Creates an array for storing scores
buildscoreTrack();

//Regular click event
$('td button').click(function(){

  //Finding the last empty button and populating it
  var buttons = $(this).parent().children('button');
  for (var i = 5; i >= 0; i--) {
    if (buttons.eq(i).css('background-color') == 'rgb(128, 128, 128)') {
      buttons.eq(i).css('background-color', document.playerTurn);
      document.scoreTrack[$(this).parent().prop('cellIndex')][i]
      = document.playerTurn.charAt(0);

      if (checkWinner()) {
        $('#subtitle').text(document.playerTurn + ' wins!');
      } else if (boardFull()) {
        $('#subtitle').text('Board is full. Draw.');
      } else{
        changeTurn();
      }
      break
    }
  }
})

//Restart button
$('.btn').click(function(){
  $('td button').css('background-color', 'gray');
  buildscoreTrack()
  $('#subtitle').text(document.playerTurn + ' turn');
})

//Change turn function
function changeTurn(){
  if (document.playerTurn == 'Red') {
    document.playerTurn = 'Blue';
  }else {
    document.playerTurn = 'Red';
  }
  $('#subtitle').text(document.playerTurn + ' turn');
}

//Check winner function
function checkWinner(){
  var myList = [];
  var yb = document.scoreTrack;
  //Checks every item of list is same
  function checkSame(x){
    return x == myList[0] && x != 'g';
  }

  //Start with vertical wins
  for (var i = 0; i < 7; i++) {
    for (var y = 0; y < 3; y++) {
      myList = yb[i].slice(y, y+4);
      if (myList.every(checkSame)) {
        return true;
      }
    }
  }

  //Check for horizontal wins
  for (var i = 0; i < 6; i++) {
    for (var y = 0; y < 4; y++) {
      myList = [yb[y][i], yb[y+1][i], yb[y+2][i], yb[y+3][i]];
      if (myList.every(checkSame)) {
        return true;
      }
    }
  }

  //Left leaning diagonals
  for (var i = 0; i < 4; i++) {
    for (var y = 0; y < 3; y++) {
      myList = [yb[i][y], yb[i+1][y+1], yb[i+2][y+2], yb[i+3][y+3]];
      if (myList.every(checkSame)) {
        return true;
      }
    }
  }

  //Right leaning diagonals
  for (var i = 0; i < 4; i++) {
    for (var y = 5; y >= 3; y--) {
      myList = [yb[i][y], yb[i+1][y-1], yb[i+2][y-2], yb[i+3][y-3]];
      if (myList.every(checkSame)) {
        return true;
      }
    }
  }
}

//Check if board is full
function boardFull(){
  for (var i = 0; i < 7; i++) {
    if (!document.scoreTrack[i].every(function(x){
      return x != 'g';
    })) {
      return false;
    }
  }
  return true;
}

//Builds an empty score tracker
function buildscoreTrack(){
  document.scoreTrack = [];
  for (var i = 0; i < 7; i++) {
    var subList = [];
    for (var y = 0; y < 6; y++) {
      subList.push('g');
    }
    document.scoreTrack.push(subList);
  }
}
