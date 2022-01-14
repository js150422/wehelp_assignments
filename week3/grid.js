let header = document.querySelector('header');
let section = document.querySelector('section');
let requestURL = 'json/superheroes.json';
let request = new XMLHttpRequest();
request.open('GET', 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json');
request.responseType = 'text';
request.send();
    
request.onload = function() {
    let viewpointText = request.response;
    let viewpoint = JSON.parse(viewpointText);

    
    for (i=0;i<16;i++){
        //沒隱藏的部分
        let vp=document.createElement('div')
        vp.className="t";
        vp.textContent=viewpoint['result']['results'][i]['stitle'];

        let photo = document.createElement('img');
        photo.src = "https"+viewpoint["result"]["results"][i]["file"].split('https')[1];  

        let myvp = document.createElement('div');
        myvp.className="p"
        if(i>7){myvp.setAttribute("id","np");}  
        
        myvp.appendChild(photo);
        myvp.appendChild(vp);

        let current=document.getElementsByClassName('grid')[0].appendChild(myvp); 
    } 
    
}

function change(){
    let elms = document.querySelectorAll("[id='np']");
    for(let i = 0; i < elms.length; i++) {
      elms[i].style.display='block'}
}   
