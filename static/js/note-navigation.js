function closeNote(note_id) {
    var list = document.getElementById("project-"+note_id).getElementsByTagName("ul")[0];
    var button = document.getElementById("project-"+note_id).getElementsByTagName("button")[0];
    var icon = button.getElementsByTagName("span")[0];
    if (!!list) {
        list.style.display = "none";
    }
    icon.classList.remove("fa-caret-down");
    icon.classList.add("fa-caret-right");
    button.onclick = function () { openNote(note_id); };
}

function openNote(note_id) {
    var list = document.getElementById("project-"+note_id).getElementsByTagName("ul")[0];
    var button = document.getElementById("project-"+note_id).getElementsByTagName("button")[0];
    var icon = button.getElementsByTagName("span")[0];
    if (!!list) { 
        list.style.display = "block"; 
    }
    icon.classList.remove("fa-caret-right");
    icon.classList.add("fa-caret-down");
    button.onclick = function () { closeNote(note_id); };
}

function selectNote(note_title, note_contents) {
    var info = document.getElementById("current-note-contents");
    var title = info.getElementsByTagName("h2")[0];
    var desc = info.getElementsByTagName("p")[0];
    title.innerHTML = note_title;
    desc.innerHTML = note_contents;
}