$(document).ready(function() {
    $.getJSON("/static/countries.json", {}, function (countries) {
        $("#id_country").autocomplete({
            source: countries
        });
    });

    $("#id_city").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "http://ws.geonames.org/searchJSON",
                dataType: "jsonp",
                data: {
                    featureClass: "P",
                    maxRows: 10,
                    name_startsWith: request.term,
                    username: "rogargon"
                },
                success: function( data ) {
                    response( $.map( data.geonames, function( item ) {
                        return {
                            label: item.name + (item.adminName1 ? ", " + item.adminName1 : "") + ", " + item.countryName,
                            value: item.name,
                            stateOrProvince: item.adminName1,
                            countryName: item.countryName
                        }
                    }));
                }
            });
        },
        minLength: 2,
        select: function( event, ui ) {
            if (ui.item) {
                $("#id_stateOrProvince").val(ui.item.stateOrProvince);
                $("#id_country").val(ui.item.countryName);
                $("#id_zipCode").val("");
            }
        }
    });
});