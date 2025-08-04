const simpleParallax = (elem, modifier) => {
    let paras = document.getElementsByClassName(elem);
    for (let i = 0; i < paras.length; i++) {
        paras[i].setAttribute('style', 'background-repeat: no-repeat; background-attachment: fixed; background-size: cover;background-position: center center;');
    }
    const sp = () => {
        for (let i = 0; i < paras.length; i++) {
            let x = paras[i].getBoundingClientRect().top / modifier;
            let y = Math.round(x * 100) / 100;
            paras[i].style.backgroundPosition = 'center ' + y + 'px';
        }
        requestAnimationFrame(sp);
    }
    requestAnimationFrame(sp);
}

simpleParallax("projects", 6)
simpleParallax("about-second-img", 8)
simpleParallax("services-process", 8)
simpleParallax("services-proud", 6)
simpleParallax("contactcontainer", 6)