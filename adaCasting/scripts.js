var mapInitialized = false;



window.onload = (event) => {
    console.log("page is fully loaded");
    doughnutChart()
    mapInteractive()
    BarChart()
    
        
  };

document.getElementById("clickMe").onclick = function () { alert('hello!'); };

function changeColor() {
  alert('hello!');
}

function callModelForest() {
  fetch("https://yannax.pythonanywhere.com/api", {
    method: 'POST',
     headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify({'name': 'salam'})
}).then(response => response.json())  
.then(json => {
    console.log(json);
})
}






document.addEventListener('DOMContentLoaded', function () {
    // Sélectionne l'élément avec la classe .scroll-down
    let scrollDown = document.querySelector('.scroll-down');

    // Ajoute un écouteur d'événements sur le clic de l'indicateur de défilement
    scrollDown.addEventListener('click', function () {
        // Fait défiler la fenêtre vers le bas de la page de manière fluide
        window.scroll({
            top: window.innerHeight,
            behavior: 'smooth'
        });

        // Initialise la variable arcs avant de générer les graphiques
        arcs = null;

        // Ajoutez le code pour générer les deux graphiques ici
         
        
        // generateMap();
    });
});

// TRANSITION 
// Fonction pour effectuer des actions une fois que le document est prêt

$(document).on("scroll", function() {
  var pageTop = $(document).scrollTop();
  var pageBottom = pageTop + $(window).height();
  var tags = $(".tag");

  for (var i = 0; i < tags.length; i++) {
    var tag = tags[i];

    if ($(tag).position().top < pageBottom) {
      $(tag).addClass("visible");
    } else {
      $(tag).removeClass("visible");
    }
  }
});

// TRANSITION 



// TRANSITION 



let arcs; // Déclaration de la variable arcs dans le contexte global



 function doughnutChart() {
    const ctx = document.getElementById('myChart');
    const data = {

        labels : [
          'Drama', 'Comedy', 'Romance Film', 'Thriller', 'Action', 'Adventure', 'Black-and-white', 'Crime Fiction', 'World cinema', 'Indie', 'Short Film', 'Horror', 'Family Film', 'Musical', 'Mystery', 'Documentary', 'Silent film', 'Science Fiction', 'Fantasy', 'Animation', 'Crime Thriller', 'War film', 'Japanese Movies', 'Western', 'Period piece'
        ],
        datasets: [{
          label: 'Number of movies',
          data: [15699, 8606, 5586, 4678, 4646, 4477, 3973, 3530, 3106, 3024, 2444, 2328, 2303, 1945, 1793, 1713, 1645, 1603, 1558, 1340, 1246, 1237, 1164, 1116, 1094],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(153, 102, 255)',
            'rgb(255, 159, 64)',
            'rgb(201, 203, 207)',
            'rgb(255, 77, 77)',
            'rgb(122, 102, 255)'
          ],
          hoverOffset: 30, // Augmentez l'offset au survol pour un effet plus visible
          borderWidth: 2, // Ajoutez une bordure autour du diagramme pour plus de clarté
          borderColor: 'rgba(255,255,255,0.8)' // Couleur de la bordure
      }]
  };
    const config = {
        type: 'doughnut',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        font: {
                            size: 14
                        }
                    }
                }
            },
            layout: {
                padding: {
                    top : 20,
                    bottom: 20 // Ajoutez de l'espace en bas du graphique

                }
            }
        }
    };

    new Chart(ctx, config);
}






 

 function BarChart() {
    const ctx = document.getElementById('barChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['<1920', '1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010-'],
      datasets: [{
        label: '# of Movies per decade',
        data: [820, 1323, 2417, 2056, 2214, 2043, 2360, 3029, 4659, 9991, 1678],
        backgroundColor: [
          'rgba(173, 216, 230, 0.2)',  // Light Sky Blue
          'rgba(135, 206, 250, 0.2)',  // Light Steel Blue
          'rgba(70, 130, 180, 0.2)',   // Steel Blue
          'rgba(138, 43, 226, 0.2)',   // Blue Violet
          'rgba(255, 0, 0, 0.2)',      // Red
          'rgba(255, 165, 0, 0.2)',    // Orange
          'rgba(255, 255, 0, 0.2)',    // Yellow
          'rgba(0, 128, 0, 0.2)',      // Green
          'rgba(0, 0, 255, 0.2)',      // Blue
          'rgba(128, 0, 128, 0.2)',    // Purple
          'rgba(255, 182, 193, 0.2)'   // Light Pink
        ],
        borderColor: [
          'rgb(173, 216, 230)',  // Light Sky Blue
          'rgb(135, 206, 250)',  // Light Steel Blue
          'rgb(70, 130, 180)',   // Steel Blue
          'rgb(138, 43, 226)',   // Blue Violet
          'rgb(255, 0, 0)',      // Red
          'rgb(255, 165, 0)',    // Orange
          'rgb(255, 255, 0)',    // Yellow
          'rgb(0, 128, 0)',      // Green
          'rgb(0, 0, 255)',      // Blue
          'rgb(128, 0, 128)',    // Purple
          'rgb(255, 182, 193)'   // Light Pink
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      },
      plugins: {
        legend: {
          display: true,
          position: 'top', // Position de la légende
          labels: {
            color: 'black' // Couleur du texte de la légende
          }
        },
        title: {
          display: true,
          text: 'Number of Movies per Decade', // Titre du graphique
          color: 'black' // Couleur du texte du titre
        }
      }
    }
  });
}



 function mapInteractive() {
    google.charts.load('current', {
        'packages':['geochart'],
      });
      google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {
        var data = google.visualization.arrayToDataTable([
          ['Country', 'Number of movies '],
          ['United States', 17995],
          ['United Kingdom', 3272],
          ['France', 2204],
          ['Germany', 1768],
          ['India', 1763],
          ['Japan', 1395],
          ['Italy', 1276],
          ['Canada', 1087],
          ['South Korea', 639],
          ['Spain', 523],
          ['Australia', 485],
          ['Denmark', 439],
          ['Sweden', 422],
          ['Hong Kong', 377],
          ['Netherlands', 334],
          ['Argentina', 263],
          ['Czech Republic', 249],
          ['Russia', 235],
          ['China', 222],
          ['Mexico', 200],
          ['Serbia', 193],
          ['Norway', 189],
          ['Belgium', 159],
          ['Poland', 157],
          ['Ireland', 139],
          ['New Zealand', 139],
          ['Hungary', 135],
          ['Switzerland', 130],
          ['Austria', 129],
          ['Finland', 124],
          ['Brazil', 114],
          ['Philippines', 108],
          ['Turkey', 104],
          ['Portugal', 83],
          ['Thailand', 80],
          ['South Africa', 78],
          ['Israel', 67],
          ['Greece', 59],
          ['Taiwan', 58],
          ['Bulgaria', 55],
          ['Indonesia', 52],
          ['Romania', 47],
          ['Croatia', 47],
          ['Luxembourg', 44],
          ['Iran', 43],
          ['Iceland', 41],
          ['Egypt', 39],
          ['Malaysia', 37],
          ['Pakistan', 31],
          ['Singapore', 27],
          ['Chile', 24],
          ['Morocco', 23],
          ['Colombia', 22],
          ['Algeria', 20],
          ['Slovakia', 20],
          ['Scotland', 18],
          ['Slovenia', 17],
          ['Estonia', 16],
          ['Bangladesh', 14],
          ['Cuba', 13],
          ['Bosnia and Herzegovina', 12],
          ['Cambodia', 12],
          ['Tunisia', 12],
          ['Vietnam', 12],
          ['Lithuania', 11],
          ['Ukraine', 11],
          ['Venezuela', 11],
          ['Lebanon', 10],
          ['United Arab Emirates', 9],
          ['Puerto Rico', 9],
          ['Peru', 9],
          ['Sri Lanka', 9],
          ['Korea', 8],
          ['Uruguay', 7],
          ['Republic of Macedonia', 7],
          ['Azerbaijan', 7],
          ['Burkina Faso', 7],
          ['Afghanistan', 7],
          ['Jamaica', 6],
          ['Albania', 6],
          ['Serbia and Montenegro', 6],
          ['Mali', 6],
          ['Democratic Republic of the Congo', 6],
          ['Palestinian territories', 6],
          ['Senegal', 5],
          ['Mandatory Palestine', 5],
          ['Kenya', 5],
          ['Slovak Republic', 5],
          ['Cameroon', 5],
          ['Iraq', 4],
          ['Armenia', 4],
          ['Malta', 4],
          ['Bolivia', 4],
          ['Bhutan', 3],
          ['Cyprus', 3],
          ['Panama', 3],
          ['Burma', 3],
          ['Aruba', 3],
          ['Monaco', 3],
          ['Nepal', 3],
          ['Wales', 3],
          ['Isle of Man', 3],
          ['Costa Rica', 3],
          ['Zambia', 2],
          ['Georgia', 2],
          ['Montenegro', 2],
          ['Bahamas', 2],
          ['Nigeria', 2],
          ['Uzbekistan', 2],
          ['Ethiopia', 2],
          ['Libya', 2],
          ['Kuwait', 2],
          ['Bahrain', 2],
          ['Zimbabwe', 2],
          ['Guinea-Bissau', 1],
          ['Uzbek SSR', 1],
          ['Georgian SSR', 1],
          ['Congo', 1],
          ['Qatar', 1],
          ['Northern Ireland', 1],
          ['Mongolia', 1],
          ['Jordan', 1],
          ['Haiti', 1],   
        ]);

        var options = {
          colors: ['#DCFFFB','#0DA0FF','#009BFF','#0068FF','#002BFF','#6800FF'],
          values: [0, 100, 200, 300, 400], // Définir les intervalles correspondants aux couleurs
          // legend: 'none', // masquer la légende de la couleur
        };

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
        // Créer une légende personnalisée
        var legend = document.getElementById('legend');
        var colors = ['#FFFFFF', '#ADD8E6', '#87CEEB', '#1E90FF', '#0000FF'];
        var labels = ['0-100', '101-200', '201-300', '301-400', '401+'];

        for (var i = 0; i < colors.length; i++) {
            var label = document.createElement('div');
            label.className = 'legend-label';
            label.style.backgroundColor = colors[i];
            label.appendChild(document.createTextNode(labels[i]));
            legend.appendChild(label);
        }
    }
}



anychart.onDocumentReady(function () {
  // The data used in this sample can be obtained from the CDN
  // https://cdn.anychart.com/samples/maps-choropleth/world-women-suffrage-map/data.json
  anychart.data.loadJsonFile(
    'https://cdn.anychart.com/samples/maps-choropleth/world-women-suffrage-map/data.json',
    function (data) {
      anychart.palettes
        .distinctColors()
        .items([
          '#fff59d',
          '#fbc02d',
          '#ff8f00',
          '#ef6c00',
          '#bbdefb',
          '#90caf9',
          '#64b5f6',
          '#42a5f5',
          '#1e88e5',
          '#1976d2',
          '#1565c0',
          '#01579b',
          '#0097a7',
          '#00838f'
        ]);
      // The data used in this sample can be obtained from the CDN
      // https://cdn.anychart.com/samples/maps-choropleth/world-women-suffrage-map/data.js
      var dataSet = anychart.data.set(data);

      var mapData = dataSet.mapAs({ description: 'description' });

      var map = anychart.map();

      // set map settings
      map
        .geoData('anychart.maps.world')
        .legend(false)
        .interactivity({ selectionMode: 'none' });

      map
        .title()
        .enabled(true)
        .fontSize(16)
        .padding(0, 0, 30, 0)
        .text('Women First Granted Suffrage at National Level (by Year)');

      map
        .credits()
        .enabled(true)
        .url('https://en.wikipedia.org/wiki/Women_suffrage')
        .text(
          'Data source: https://en.wikipedia.org/wiki/Women_suffrage/'
        )
        .logoSrc('https://en.wikipedia.org/static/favicon/wikipedia.ico');

      var series = map.choropleth(mapData);
      series.geoIdField('iso_a2').labels(false);
      series.hovered().fill('#455a64');
      var scale = anychart.scales.ordinalColor([
        { less: 1907 },
        { from: 1907, to: 1920 },
        { from: 1920, to: 1940 },
        { from: 1940, to: 1950 },
        { from: 1950, to: 1960 },
        { from: 1960, to: 1970 },
        { from: 1970, to: 1980 },
        { greater: 1980 }
      ]);

      scale.colors([
        '#42a5f5',
        '#64b5f6',
        '#90caf9',
        '#ffa726',
        '#fb8c00',
        '#f57c00',
        '#ef6c00',
        '#e65100'
      ]);
      series.colorScale(scale);

      var colorRange = map.colorRange();
      colorRange
        .enabled(true)
        .padding([20, 0, 0, 0])
        .colorLineSize(5)
        .marker({ size: 7 });
      colorRange
        .ticks()
        .enabled(true)
        .stroke('3 #ffffff')
        .position('center')
        .length(20);
      colorRange
        .labels()
        .fontSize(10)
        .padding(0, 0, 0, 5)
        .format(function () {
          var range = this.colorRange;
          var name;
          if (isFinite(range.start + range.end)) {
            name = range.start + ' - ' + range.end;
          } else if (isFinite(range.start)) {
            name = 'After ' + range.start;
          } else {
            name = 'Before ' + range.end;
          }
          return name;
        });

      map
        .tooltip()
        .useHtml(true)
        .format(function () {
          var result;
          var value = '<span>';
          var description = '<br/><span>';
          if (this.value === '20000') {
            result = value + 'Never</span></strong>';
          } else result = value + this.value + '</span></strong>';

          if (
            getDescription(this.id) !== undefined &&
            getDescription(this.id) !== ''
          ) {
            result =
              result +
              description +
              getDescription(this.id) +
              '</span></strong>';
          }
          return result;
        });

      // create zoom controls
      var zoomController = anychart.ui.zoom();
      zoomController.render(map);

      // set container id for the chart
      map.container('container');
      // initiate chart drawing
      map.draw();

      function getDescription(id) {
        for (var i = 0; i < data.length; i++) {
          if (data[i].id === id) return data[i].description;
        }
      }
    }
  );
});


 

// Obtenez le contexte du canvas
const ctx = document.getElementById('boxPlotChart').getContext('2d');

// Initialisez le graphique avec Chart.js
const boxPlotChart = new Chart(ctx, {
  type: 'boxplot',
  data: boxPlotData,
  options: {
    responsive: true,
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Box Plot Chart',
    },
  },
});

// };



