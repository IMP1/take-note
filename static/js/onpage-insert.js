function tryInsert(id) {
    var title = document.getElementById("insert-title").value;
    if (validEdit(title)) {
        sendInsert(id, title);
        document.getElementById("insert-title").value = "";
    }
}

function validEdit(title) {
    if (!title.trim()) { return false; }
    return true;
}

function sendInsert(id, title) {
    $.ajax({ 
        type: "POST", 
        url: "http://127.0.0.1:8000/TakeNote/project/insert", 
        cache: false,
        data: { id: id, title: title, description: "" }
    }).done(function( new_id ) {
        window.location.assign("http://127.0.0.1:8000/TakeNote/project/view/" + new_id);
    });
}