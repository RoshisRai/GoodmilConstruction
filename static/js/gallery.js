$(document).ready(function(){
    $(window).on('load', function(){
        var $container = $('.filter-container');
        $container.isotope({
            filter: '*',
            animationOptions: {
                queue: true
            }
        })
        
        $('.filter-menu li').click(function(){
            $('.filter-menu .current').removeClass('current');
            $(this).addClass('current')
            var selector = $(this).attr('data-filter');
            $($container).isotope({
                filter: selector,
                animationOptions: {
                    queue: true
                }
            })
            return false;
        })
    })

})


const galleryPage  = document.querySelectorAll(".image"),
previewBoxPage = document.querySelector(".preview-box"),
previewImgPage = previewBoxPage.querySelector("img"),
closeIconPage = previewBoxPage.querySelector(".icon"),
currentImgPage = previewBoxPage.querySelector(".current-img"),
totalImgPage = previewBoxPage.querySelector(".total-img"),
shadowPage = document.querySelector(".shadow");
window.onload = ()=>{
for (let i = 0; i < galleryPage.length; i++) {
totalImgPage.textContent = galleryPage.length; //passing total img length to totalImgPage variable
let newIndex = i; //passing i value to newIndex variable
let clickedImgIndex; //creating new variable

function galleryTriggerFunction(i){
    clickedImgIndex = i; //passing cliked image index to created variable (clickedImgIndex)
    function preview(){
        currentImgPage.textContent = newIndex + 1; //passing current img index to currentImgPage varible with adding +1
        let imageURL = galleryPage[newIndex].querySelector("img").src; //getting user clicked img url
        previewImgPage.src = imageURL; //passing user clicked img url in previewImgPage src
    }
    preview(); //calling above function

    const prevBtn = document.querySelector(".pre");
    const nextBtn = document.querySelector(".nex");
    if(newIndex == 0){ //if index value is equal to 0 then hide prevBtn
        prevBtn.style.display = "none"; 
    }
    if(newIndex >= galleryPage.length - 1){ //if index value is greater and equal to galleryPage length by -1 then hide nextBtn
        nextBtn.style.display = "none"; 
    }
    prevBtn.onclick = ()=>{ 
        newIndex--; //decrement index
        if(newIndex == 0){
            preview(); 
            prevBtn.style.display = "none"; 
        }else{
            preview();
            nextBtn.style.display = "block";
        } 
    }
    nextBtn.onclick = ()=>{ 
        newIndex++; //increment index
        console.log('hello next')
        if(newIndex >= galleryPage.length - 1){
            preview(); 
            nextBtn.style.display = "none";
        }else{
            preview(); 
            prevBtn.style.display = "block";
        }
    }
    
    document.querySelector("body").style.overflow = "hidden";
    previewBoxPage.classList.add("show"); 
    shadowPage.style.display = "block"; 
    closeIconPage.onclick = ()=>{
        newIndex = clickedImgIndex; //assigning user first clicked img index to newIndex
        prevBtn.style.display = "block"; 
        nextBtn.style.display = "block";
        previewBoxPage.classList.remove("show");
        shadowPage.style.display = "none";
    }
}

galleryPage[i].onclick = () =>{
    galleryTriggerFunction(i)
}
galleryPage[i].nextElementSibling.onclick = () =>{
    galleryTriggerFunction(i)
}
galleryPage[i].nextElementSibling.nextElementSibling.onclick = () =>{
    galleryTriggerFunction(i)
}

} 
}