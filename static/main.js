/*jshint esversion: 8 */


// jQuery(document).ready(function ($) {


var input_siret = document.getElementById("searchBar");
// var numero_siret = input_siret.value;
var numero_siret = {};


// Appel de la route flask pour transmettre le numero siret entré par l'utilisateur:
$('#searchBtn').click(function () {
    if (input_siret.value != '') {
        numero_siret.key = input_siret.value;
    }
    (async () => {
        data = await fetch('/search', {
            method: "post",
            credentials: "same-origin",
            body: numero_siret,
            cache: "no-cache"
        })
            .then(data => {
                listeDesResultats = data
                console.log(listeDesResultats);
            }).catch(err => console.log('Failed la récupération des resultats', err))
    });

});

