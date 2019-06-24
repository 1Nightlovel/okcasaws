
$(document).ready(function(){
    var Togglecon = 0;
   $('#panelexpander').click(function(){
     console.log("rf")
    if (Togglecon==0 ) {
      Togglecon = 1;
      $('#addpanel').removeClass('expanded');
      $('#addpanel').addClass('unexpand');
    } else if (Togglecon==1) {
      Togglecon = 0;
      $('#addpanel').removeClass('unexpand');
      $('#addpanel').addClass('expanded');
    } 
      
  });
  }); 