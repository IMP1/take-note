var editableInfo = document.getElementById("note-info");
var editableForm = document.getElementById("note-info-edit");
var button = document.getElementById("edit-toggle-button");

function openEditView() {
    button.innerHTML = "Cancel";
    button.onclick = function() {
        closeEditView();
    }
    editableInfo.style.display = "none";
    editableForm.style.display = "block";
}

function closeEditView() {
    button.innerHTML = "Edit";
    button.onclick = function() {
        openEditView();
    }
    editableForm.style.display = "none";
    editableInfo.style.display = "block";
}

function tryEdit(id) {
    var newTitle = document.getElementById("edit-title").value;
    var newDescription = document.getElementById("edit-description").value;
    if (validEdit(newTitle, newDescription)) {
        sendEdit(id, newTitle, newDescription);
    }
}

function validEdit(newTitle, newDescription) {
    if (!newTitle.trim()) { return false; }
    var oldTitle = editableInfo.getElementsByTagName("h1")[0].innerHTML.trim();
    var oldDescription = editableInfo.getElementsByTagName("p")[0].innerHTML.trim();
    if (newTitle.trim() == oldTitle && newDescription.trim() == oldDescription) { return false; }
    return true;
}

function sendEdit(id, newTitle, newDescription) {
    $.ajax({ 
        type: "POST", 
        url: "http://127.0.0.1:8000/TakeNote/project/edit", 
        cache: false ,
        data: { id: id, title: newTitle, description: newDescription }
    }).done(function( html_string ) {
        editableInfo.innerHTML = html_string;
        closeEditView();
    });
}