function menu() {
    const addCSS = css => document.head.appendChild(document.createElement("style")).innerHTML=css;
    addCSS(`.navigation__home {
        margin-left: 50px;
    }
    
    .navigation__garage {
        margin-left: -40px;
    }
    
    .navigation__gallery {
        margin-left: -90px;
    }
    
    .navigation__contacts {
        margin-left: -160px;
    }
    @media screen and (max-width: 810px){
        .sidebar {
            right: 0px;
        }
    }
    `
    );

    
}

menu();