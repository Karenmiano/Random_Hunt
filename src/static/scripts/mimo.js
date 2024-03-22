setTimeout(() => {
    new TypeIt("#mimo_title", {
        speed: 110,
        waitUntilVisible: true,
        nextStringDelay: [500, 1000],
        afterComplete: function (instance) {
            instance.destroy();
        }
    }).type("Finding Mimo")
       .exec(async () => {
           await new Promise((resolve, reject) => {
                setTimeout(() => {
                    new TypeIt("#mimo_description", {
                        speed: 110,
                        waitUntilVisible: true,
                        nextStringDelay: [500, 1000],
                        afterComplete: function (instance) {
                            instance.destroy();
                        }
                    }).type("<em>Journey across the universe</em>")
                        .exec(async () => {
                            await new Promise((resolve, reject) => {
                                setTimeout(() => {
                                    return resolve();
                                }, 2000); 
                            });
                        })
                        .type(",<em>  journey<br>towards yourself.</em>")
                        .exec(() => {
                            setTimeout(() => {
                                const getOnboard = document.getElementById("get_started");
                                getOnboard.classList.remove("invisible");
                                getOnboard.style.animation = "slideUp 0.5s ease-out forwards";
                            }, 500);
                        })
                        .go();
            
                        resolve();
                }, 1600);
           });
       })
       .go();
}, 1000);

