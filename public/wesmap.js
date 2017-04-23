/*
    This is not used anymore
*/
var request = new XMLHttpRequest();
request.open("GET", "cs.json", false);
request.send();
var wesmap_JSON = JSON.parse(request.responseText)
var allSearch = []

function dedup(arr) {
    arr = arr.filter( function( item, index, inputArray ) {
           return inputArray.indexOf(item) == index;
    });
    return arr
}

for (var key in wesmap_JSON) {
  if (wesmap_JSON.hasOwnProperty(key)) {
    var major_JSON = wesmap_JSON[key]
    var major = document.querySelector("#".concat(Object.keys(major_JSON)[0]));
    var deduped = [];
    $.each(major_JSON[Object.keys(major_JSON)[0]], function(i, el){
      if($.inArray(el, deduped) === -1) {
          deduped.push(el);
          allSearch.push(el);
      }
    });
    var comma = deduped.join(", ");
    major.innerHTML = comma;
  }
}


allSearch = dedup(allSearch)
$("#course-name-input").autocomplete({
    source: allSearch
});
