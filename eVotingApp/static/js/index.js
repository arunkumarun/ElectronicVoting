$("input[type='radio']").on('change',function(){
    if($(this).val() == "senate")
       $('.box').show('slow');
    else
        $('.box').show('slow');
});