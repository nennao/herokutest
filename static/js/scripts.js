$( "#button" ).click(function() {
  // alert( "nice" );
  fetch('https://safe-crag-49936.herokuapp.com/data/random')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(JSON.stringify(myJson['random']));
  });
});

$( "#button2" ).click(function() {
  // alert( "nice" );
  fetch('https://safe-crag-49936.herokuapp.com/data/post?name=nemes', {method: 'POST'})
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(JSON.stringify(myJson));
  });
});

const rawData = {"2017-12-31":13860.1363,"2018-01-01":13412.44,"2018-01-02":14740.7563,"2018-01-03":15134.6513,"2018-01-04":15155.2263,"2018-01-05":16937.1738,"2018-01-06":17135.8363,"2018-01-07":16178.495,"2018-01-08":14970.3575,"2018-01-09":14439.4738,"2018-01-10":14890.7225,"2018-01-11":13287.26,"2018-01-12":13812.715,"2018-01-13":14188.785,"2018-01-14":13619.0288,"2018-01-15":13585.9013};


function parseData(data) {
  let arr = [];
  for (let i in Object.keys(data)) {
    arr.push({
      date: new Date(i),
      value: +data[i]
    });
  }
  return arr
}

let data = parseData(rawData);

function drawChart(data) {
  const svgWidth = 600, svgHeight = 400;
  const margin = {top: 20, right: 20, bottom: 30, left: 50};
  const width = svgWidth - margin.left - margin.right;
  const height = svgHeight - margin.top - margin.bottom;

  const svg = d3.select('#testD3').attr("width", svgWidth).attr("height", svgHeight);
}