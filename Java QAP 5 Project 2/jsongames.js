fetch('./games.json')
    .then(response => response.json()) // This "converts" the .json file so it can be read in the .js
    .then(games => {
        for(let i = 0; i < games.length; i++){ // a for loop can be used to find a specific key/value pair of the array, using i to decide how many of the objects you want to select
            console.log(games[i].title)
        }
    })

fetch('./games.json')
    .then(response => response.json())
    .then(games => {
        games.forEach(game => { // a forEach loop can be used to display each of the entire objects in the array.
            console.log(game)
        })
    })

fetch('./games.json')
    .then(response => response.json())
    .then(games => {
        games.forEach(game => {
            getGenre(game); // set up the function here then define it outside of the method.
        });
    })
    .catch(error => {
        // Handle errors that occur while fetching the file
        console.error(error);
    });

function getGenre(game) {
    switch (game.genre) { // switch can be used to target a specific key in the array then isolate each of the different values.
        case "MMORPG":
            console.log(`Fans of the MMO genre should play ${game.title}.`)
            break;
        case "extraction":
            console.log(`Fans of the extraction genre should play ${game.title}.`)
            break;
        case "asymmetrical survival/horror":
            console.log(`Fans of the asymmetrical survival/horror genre should play ${game.title}.`)
            break;
        case "metroidvania":
            console.log(`Fans of the metroidvania genre should play ${game.title}.`)
            break;
    }
};