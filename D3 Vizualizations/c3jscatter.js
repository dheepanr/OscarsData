var chart = c3.generate({
    data: {
        xs: {
            Action: 'Action_x',
            Mystery: 'Mystery_x',
            Sports:'Sports_x',
            SciFi:'SciFi_x',
            Musical:'Musical_x',
            Family: 'Family_x',
            Animation: 'Animation_x',
            Western: 'Western_x',
            Biography: 'Biography_x',
            Drama: 'Drama_x',
            Thriller: 'Thriller_x',
            Romance: 'Romance_x',
            Adventure: 'Adventure_x',
            Comedy: 'Comedy_x',
            Crime: 'Crime_x',
            History: 'History_x',
            War: 'War_x',
            Fantasy: 'Fantasy_x'



        
        },
       
        columns: [
            ["Action", 70.14],
            ["Mystery",81.78],
            ["Sports",83.6],
            ["SciFi",71.0],
            ["Musical",81.0],
            ["Family",93.5],
            ["Animation",98.5],
            ["Western",92.0],
            ["Biography",84.22],
            ["Drama",82.11],
            ["Thriller",88.67],
            ["Romance",69.95],
            ["Adventure",88.93],
            ["Comedy",85.69],
            ["Crime",87.25],
            ["History",82.21],
            ["War", 87.1],
            ["Fantasy",87.73],

            ["Action_x", 86.0],
            ["Mystery_x",81.0],
            ["Sports_x",85.2],
            ["SciFi_x",71.4],
            ["Musical_x",86.0],
            ["Family_x",86.0],
            ["Animation_x",89.5],
            ["Western_x",88.0],
            ["Biography_x",82.59],
            ["Drama_x",81.03],
            ["Thriller_x", 84.94],
            ["Romance_x", 76.32],
            ["Adventure_x",84.4],
            ["Comedy_x",77.19],
            ["Crime_x",83.25],
            ["History_x",78.64],
            ["War_x",84.3],
            ["Fantasy_x",83.91]
        ],
        type: 'scatter'
    },
    axis: {
        x: {
            label: 'Audience Score',
            tick: {
                fit: false
            }
        },
        y: {
            label: 'Critic Score'
        }
    },
    tooltip: {
        format: {
            title: function (d) { return 'Genre Critic Score'; }
            
            }
        },
    point :{r:15}
});



