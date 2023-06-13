
function updateStatus(){
    console.log("ok");
    var mySelect = document.getElementById('choice');
    mySelect.onchange = (event) => {
        var pk = event.target.parentNode.parentNode;
        subbmiter = document.getElementById('submitter');
        subbmiter.value = [pk.id, event.target.value]
        document.getElementById("form").submit(); 
    } 
};



function openWindow(){
    window.open('/service/cars/add-queue', 'Queue Form', 'width=600,height=450'); return false;
}