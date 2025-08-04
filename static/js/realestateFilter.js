//For location Filter
const optionMenuLocation = document.querySelector(".select-menu-location"),
selectBtnLocation = optionMenuLocation.querySelector(".select-btn-location"),
optionsLocation = optionMenuLocation.querySelectorAll(".option-location"),
sBtn_textLocation = optionMenuLocation.querySelector(".sBtn-text-location"),
inputPropertyLocation = document.querySelector('#property-location');

selectBtnLocation.addEventListener("click", () => optionMenuLocation.classList.toggle("active"));       

optionsLocation.forEach(option =>{
    option.addEventListener("click", ()=>{
        let selectedOption = option.querySelector(".option-text-location").innerText;
        sBtn_textLocation.innerText = selectedOption;
        
        optionMenuLocation.classList.remove("active");
        inputPropertyLocation.setAttribute('value', selectedOption)
    });
});

document.addEventListener('mouseup', function(e) {
    if (!optionMenuLocation.contains(e.target)) {
        optionMenuLocation.classList.remove("active");
        // inputPropertyLocation.setAttribute('value', "")
    }
});

//For type Filter
const optionMenuType = document.querySelector(".select-menu-type"),
selectBtnType = optionMenuType.querySelector(".select-btn-type"),
optionsType = optionMenuType.querySelectorAll(".option-type"),
sBtn_textType = optionMenuType.querySelector(".sBtn-text-type"),
inputPropertySaleOrRent = document.querySelector('#property-sale-or-rent');

selectBtnType.addEventListener("click", () => optionMenuType.classList.toggle("active"));       

optionsType.forEach(option =>{
    option.addEventListener("click", ()=>{
        let selectedOption = option.querySelector(".option-text-type").innerText;
        sBtn_textType.innerText = selectedOption;
        
        optionMenuType.classList.remove("active");
        inputPropertySaleOrRent.setAttribute('value', selectedOption)
        
    });
});

document.addEventListener('mouseup', function(e) {
    if (!optionMenuType.contains(e.target)) {
        optionMenuType.classList.remove("active");
        // inputPropertySaleOrRent.setAttribute('value', "")
    }
});

//For property Filter
const optionMenuProperty = document.querySelector(".select-menu-property"),
selectBtnProperty = optionMenuProperty.querySelector(".select-btn-property"),
optionsProperty = optionMenuProperty.querySelectorAll(".option-property"),
sBtn_textProperty = optionMenuProperty.querySelector(".sBtn-text-property"),
inputPropertyType = document.querySelector('#property-type');

selectBtnProperty.addEventListener("click", () => optionMenuProperty.classList.toggle("active"));       

optionsProperty.forEach(option =>{
    option.addEventListener("click", ()=>{
        let selectedOption = option.querySelector(".option-text-property").innerText;
        sBtn_textProperty.innerText = selectedOption;
        
        optionMenuProperty.classList.remove("active");
        inputPropertyType.setAttribute('value', selectedOption)
        if(selectedOption === 'Interior'){
            sBtn_textType.innerText = "Sale";
            inputPropertySaleOrRent.setAttribute('value', "Sale")
            optionsType.forEach(opt=>{
                let removedOpt = opt.querySelector(".option-text-type").innerHTML
                if(removedOpt=='Rent'){
                    opt.style.display = 'none'
                }
            })
        }else{
            optionsType.forEach(opt=>{
                sBtn_textType.innerHTML = "<i class='fa-solid fa-filter-circle-dollar'></i>&nbsp; Type";
                inputPropertySaleOrRent.setAttribute('value', "")
                let removedOpt = opt.querySelector(".option-text-type").innerHTML
                if(removedOpt=='Rent'){
                    opt.style.display = 'block'
                }
            })
        }
    });
});


document.addEventListener('mouseup', function(e) {
    if (!optionMenuProperty.contains(e.target)) {
        optionMenuProperty.classList.remove("active");
        // inputPropertyType.setAttribute('value', "")
    }
});