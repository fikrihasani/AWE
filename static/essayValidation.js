var essaySubmitButton = document.querySelector('.essay-submit-button');
essaySubmitButton.addEventListener("click", essayFormValidation);

var essay = document.getElementById("essayInput")

alert("hey");

function essayFormValidation(e){
    e.preventDefault();

    var flag = 0;

    //validate all fields not empty
    if(essay.value == '' ){
        flag = 1;
    }
    else alert(essay.value);

    if(flag==1){
        alert("hey");
        return false;
    }
    else{
        var essayForm = document.getElementById('essayForm');
        essayForm.submit();
    }
}