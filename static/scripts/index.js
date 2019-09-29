const microphone = document.querySelector('.listen');
const tags = document.querySelector(".result-tags");
const inputs = document.querySelectorAll(".form-control");


function add_tags(response){
    for (var key in response) {
        if (response.hasOwnProperty(key)) {
            tags.innerHTML += "	<div class = 'card tag m-l-20 m-r-20 m-b-20'> <h2 class ='key-vals'>" + key + ": " +response[key] + " </h2> </div>"    
        }
    }
    for(var i = 0; i < inputs.length; i++){
        if(inputs[i].id in response){
            inputs[i].value = response[inputs[i].id];
        }
    }
}

microphone.addEventListener('click', (e)=>{
    e.preventDefault();
    $('.listen').css({
        'border-color': 'red',
        'border-width': '3px'   
    });
    $.ajax({
        url: "http://localhost:5000/parse_ems",
        data: {},
        dataType: 'json',
        success: function(response){
            $('.listen').css({
                'border-color': 'rgba(0,0,0,.125)',
                'border-width': '1px'
            });
            add_tags(response);
        },
   });
});

