function tryMove(id) {
    var new_parent = document.getElementById("move-note").value;
    sendInsert(id, new_parent);
}

function sendInsert(id, new_parent) {
    alert("sending to server...");
    $.ajax({ 
        type: "POST", 
        url: "http://127.0.0.1:8000/TakeNote/project/move", 
        cache: false,
        data: { id: id, parent: new_parent }
    }).done(function( new_id ) {
        window.location.reload();
    });
}