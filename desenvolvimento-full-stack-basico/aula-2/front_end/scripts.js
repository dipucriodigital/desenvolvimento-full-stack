// Cria um novo item na lista
function newElement(){
    var li = document.createElement("li");
    var inputValue = document.getElementById("newInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if(inputValue === ''){
        alert("Escreva o nome de um item");
    } else {
        document.getElementById("myList").appendChild(li);
    }
    document.getElementById("newInput").value = "";
}