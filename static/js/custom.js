/**
 * Created by emam on 17/09/16.
 */
function get_customer(){
    $.ajax({
        url: "/api/v1/get_customers/",
        type: 'POST',
        dataType:'JSON',
        data:{
            id:$('#id_area').val()
        },
        success: function (responseText) {
           console.log(responseText);
            populateCustomers(responseText);
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);

        }
    });
}

function populateCustomers(json){
    $('#id_customer').find('option').remove().end();
    $('#id_customer').append('<option value="" selected="selected">---------</option>');
    for (var i=0 ; i<json.length ; i++){
        $('#id_customer').append('<option value=' + json[i].pk + '>' + json[i].fields.name + '</option>');
    }
}

function get_customer_info(){
     $.ajax({
        url: "/api/v1/get_customers_info/",
        type: 'POST',
        dataType:'JSON',
        data:{
            customer_number:$('#id_customer_number').val()
        },
        success: function (responseText) {
            $('#id_area').val(JSON.parse(responseText).area_id);
            $('#id_customer').val(JSON.parse(responseText).customer_id);
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);

        }
    });
}