var tog  = document.querySelector(".toggle_btn");
var togglebtn = document.querySelector(".toggle_btn i") 
var  dropdownmenu = document.querySelector(".dropdown_menu")

tog.onclick = function(){
    dropdownmenu.classList.toggle("open")
    const isopen = dropdownmenu.classList.contains('open')
    togglebtn.classList = isopen ? 'bx bx-window-close bxtogle':'bx bx-list-ul bxtogle'
}

