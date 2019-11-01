console.log("WOrking")
$("input[type='radio']").on('change',function(){
    console.log("In WOrking")
    if($(this).val() == "senate")
       $('.box').show('slow');
    else
        $('.box').show('slow');
});