function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
};

var csrftoken = getCookie('csrftoken');

const list = document.querySelector('#maindrawer');

const maindrawer = new mdc.drawer.MDCDrawer.attachTo(list);

const list2 = document.querySelector('#messagedrawer');

const messagedrawer = new mdc.drawer.MDCDrawer.attachTo(list2);

const list3 = document.querySelector('#userdrawer');

const userdrawer = new mdc.drawer.MDCDrawer.attachTo(list3);

const topAppBarElement = document.querySelector('.mdc-top-app-bar');

const barra = new mdc.topAppBar.MDCTopAppBar.attachTo(topAppBarElement);

const fabRippleel = document.querySelector('.mdc-fab');

const fabRipple = new mdc.ripple.MDCRipple.attachTo(fabRippleel);

const settingsdialog = new mdc.dialog.MDCDialog(document.querySelector('#settingsmodal'));

const textfs = document.querySelectorAll('.mdc-text-field')

for (const textf of textfs) {
    mdc.textField.MDCTextField.attachTo(textf);
}


barra.listen('MDCTopAppBar:nav', () => {
    console.log('menu button click')
    userdrawer.open = false;
    maindrawer.open = !maindrawer.open;
  });

fabRipple.listen('click', () => {
    console.log('message button click')
    maindrawer.open = false;
    userdrawer.open = false;
    messagedrawer.open = !messagedrawer.open;
  });

function settings(){
    console.log('settings button click')
    maindrawer.open = false;
    userdrawer.open = false;
    settingsdialog.open();
};
userbutton = document.querySelector('#usericon');
const userripple = new mdc.ripple.MDCRipple.attachTo(userbutton);
userripple.listen('click', () => {
  console.log('user button click')
  maindrawer.open = false;
  userdrawer.open = !userdrawer.open;
});
  particlesJS("particles-js", {
    "particles": {
      "number": {
        "value": 100,
        "density": {
          "enable": true,
          "value_area":1000
        }
      },
      "color": {
        "value": ["#aa73ff", "#f8c210", "#83d238", "#33b1f8"]
      },
      
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0,
          "color": "#fff"
        },
        "polygon": {
          "nb_sides": 5
        },
        "image": {
          "src": "img/github.svg",
          "width": 100,
          "height": 100
        }
      },
      "opacity": {
        "value": 0.6,
        "random": false,
        "anim": {
          "enable": false,
          "speed": 1,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 2,
        "random": true,
        "anim": {
          "enable": false,
          "speed": 40,
          "size_min": 0.1,
          "sync": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 120,
        "color": "#ffffff",
        "opacity": 0.4,
        "width": 1
      },
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "grab"
        },
        "onclick": {
          "enable": false
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 140,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 400,
          "size": 40,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true
  });

  function startTime() {
    var weekdays = new Array(7);
        weekdays[0] = "Domingo";
        weekdays[1] = "Lunes";
        weekdays[2] = "Martes";
        weekdays[3] = "Miercoles";
        weekdays[4] = "Jueves";
        weekdays[5] = "Viernes";
        weekdays[6] = "Sabado";
        
    var today = new Date();
    var day = weekdays[today.getDay()];
    var number = today.getDate();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    day+" " +number+"     "+'<i class="material-icons mdc-list-item__graphic" style="color: black;vertical-align: middle;" aria-hidden="true">calendar_today</i>'+ h + ":" + m + ":" + s+'<i class="material-icons mdc-list-item__graphic" style="color: black;vertical-align: middle;" aria-hidden="true">alarm</i>';
    var t = setTimeout(startTime, 500);
  }
  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
  }

  function resend(){
    var tel = $('#teldat').val();
    $.post("/resend",{'csrfmiddlewaretoken': csrftoken,'tel':tel,},function(data){
        console.log(data.success);
        s = data.success;
        if (s){

        }
        else{
            alert(data.reason);
        }
    });
}


$('#foto').change(function(){    
  //on change event  
  formdatastep3 = new FormData();
  if($(this).prop('files').length > 0)
  {
      file =$(this).prop('files')[0];
      formdatastep3.append('foto', file);
  }
});

function changedatarelator(){
  $.post("/editarRelator2",{'csrfmiddlewaretoken': csrftoken,'nombre':$('#nombre').val(),'apellido':$('#apellido').val(),'telefono':$('#telefono').val(),'email':$('#email').val(),'foto':$('#foto').val()},function(data){
    console.log(data.success);
    console.log(data.relator);
   
    s = data.success;
  });
}


function cargarAgendar(){
  $('#content').empty();
  $('#content').load('/agendar')
  }

function cargarHistorial(){
  $('#content').empty();
  $('#content').load('/historial')
  }

function cargarCreaTecnico(){
  $('#content').empty();
  $('#content').load('/register_tecnico');
}

function cargarListado(){
  $('#content').empty();
  $('#content').load('/listado_tecnico');
}