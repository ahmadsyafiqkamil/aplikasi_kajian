var domain = "";
var subject = "";
var var_id = 0;
var th_id = 0;
var turth_id = 0;
var turvar_id = 0;
var table_var, table_turth, table_turvar, table_vervar, table_th;

$(function () {
    'use strict'

    $('.select2').select2({
        placeholder: 'Choose one',
        searchInputPlaceholder: 'Search options'
    });


    $("#id_subject").prop("disabled", true); // menonaktifkan select2 kedua saat halaman dimuat
    $('#search-button').hide();


    $("#id_domain").change(function () { // menambahkan event change pada select2 pertama
        if ($(this).val() != "") { // jika select2 pertama dipilih
            $("#id_subject").prop("disabled", false); // mengaktifkan select2 kedua
        } else {
            $("#id_subject").prop("disabled", true); // menonaktifkan select2 kedua jika select2 pertama tidak dipilih
            $('#id_subject').val('');
        }
    });

    $("#id_subject").change(function (event) {
        event.preventDefault(); // hindari form submit secara normal
        domain = $('#id_domain').val();
        subject = $('#id_subject').val();

        $('#search-button').show();
        if (table_var) {
            table_var.ajax.reload();
            return;
        }

        table_var = $('#example4').DataTable({
            ordering: false,
            responsive: true,
            processing: true,
            serverSide: true,
            ajax: {
                url: "/data_get_data/",
                type: 'POST',
                async: true,
                data: {
                    "domain": domain,
                    "subject": subject,
                    "model": "var",
                    "csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val()
                },
                dataSrc: function (json) {
                    if (json.data === "no_data") {
                        // Tampilkan pesan jika data kosong
                        alert("Data tidak tersedia");
                        return [];
                    } else {
                        return json.data;
                    }
                }
            },
            "columns": [
                {
                    "data": "title",
                    render: function (data, type, row) {
                        return '<span style="white-space:normal">' + data + "</span>";
                    }
                },

                {
                    "data": "var_id",
                    "render": function (data, type, row, meta) {
                        var idString = data.toString(); // konversi data ke dalam bentuk string
                        return '<button id="var_id" class="btn btn-outline-primary"  onclick="getDataTurVarTh(\'' + idString + '\');">' + idString + '</button>';
                    }
                },

            ],
        })
    });
    $("#search-button").on('click', () => {
        console.log('Search Button', {
            domain: domain,
            subject: subject,
            var_id: var_id,
            th_id: th_id,
            turvar_id: turvar_id
        });
        var data = {
            model: "data",
            domain: domain,
            subject: subject,
            var_id: var_id,
            th_id: th_id,
            turvar_id: turvar_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        };
        $.post("/data_get_data/", data, function (response) {
            console.log(response)
        })
    });
});

function sendth() {
    if (table_th) {
        table_th.ajax.reload();
        return;
    }
    table_th = $('#th').DataTable({
        ordering: false,
        responsive: true,
        processing: true,
        serverSide: true,
        ajax: {
            url: "/data_get_data/",
            type: 'POST',
            async: true,
            data: {
                "domain": domain,
                "model": "th",
                "id_var": var_id,
                "csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val()
            },
            dataSrc: function (json) {
                if (json.data === "no_data") {
                    // Tampilkan pesan jika data kosong
                    alert("Data tidak tersedia");
                    return [];
                } else {
                    return json.data;
                }
            }
        },
        "columns": [
            {
                "data": "th"
            },

            {
                "data": "th_id",
                "render": function (data, type, row, meta) {
                    var idString = data.toString(); // konversi data ke dalam bentuk string
                    return '<button class="btn btn-outline-primary btn-th-id" data-id="' + idString + '"> Pilih </button>';
                }
            },

        ],

    })
}

function sendturvar() {
    if (table_turvar) {
        table_turvar.ajax.reload();
        return;
    }
    table_turvar = $('#turvar').DataTable({
        ordering: false,
        responsive: true,
        processing: true,
        serverSide: true,
        ajax: {
            url: "/data_get_data/",
            type: 'POST',
            async: true,
            data: {
                "domain": domain,
                "model": "turvar",
                "id_var": var_id,
                "csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val()
            },
            dataSrc: function (json) {
                if (json.data === "no_data") {
                    // Tampilkan pesan jika data kosong
                    alert("Data tidak tersedia");
                    return [];
                } else {
                    return json.data;
                }
            }
        },
        "columns": [
            {
                "data": "turvar"
            },

            {
                "data": "turvar_id",
                "render": function (data, type, row, meta) {
                    var idString = data.toString(); // konversi data ke dalam bentuk string
                    return '<button class="btn btn-outline-primary btn-turvar-id" data-id="' + idString + '"> Pilih </button>';
                }
            },

        ],

    })
}

$(document).on('click', '.btn-th-id', function () {
    let id = $(this).data('id');
    th_id = id;
})
$(document).on('click', '.btn-turvar-id', function () {
    let id = $(this).data('id');
    turvar_id = id;
})


function getDataTurVarTh(id) {
    var_id = id;
    console.log('send', {domain: domain, subject: subject, var_id: var_id});
    // sendturth();
    sendturvar();
    sendth();
}

// ===================================================
// bisa dipakai nanti
$(document).on('click', '.btn-turth-id', function () {
    let id = $(this).data('id');
    turth_id = id;
})

function sendturth() {
    if (table_turth) {
        table_turth.ajax.reload();
        return;
    }
    table_turth = $('#turth').DataTable({
        ordering: false,
        responsive: true,
        processing: true,
        serverSide: true,
        ajax: {
            url: "/data_get_data/",
            type: 'POST',
            async: true,
            data: {
                "domain": domain,
                "model": "turth",
                "id_var": var_id,
                "csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val()
            },
            dataSrc: function (json) {
                if (json.data === "no_data") {
                    // Tampilkan pesan jika data kosong
                    alert("Data tidak tersedia");
                    return [];
                } else {
                    return json.data;
                }
            }
        },
        "columns": [
            {
                "data": "turth"
            },

            {
                "data": "turth_id",
                "render": function (data, type, row, meta) {
                    var idString = data.toString(); // konversi data ke dalam bentuk string
                    return '<button class="btn btn-outline-primary btn-turth-id" data-id="' + idString + '"> Pilih </button>';
                }
            },

        ],

    })
}

function sendVervar(id_vervar, domain) {
    if (table_vervar) {
        table_vervar.ajax.reload();
        return;
    }
    table_vervar = $('#vervar').DataTable({
        ordering: false,
        responsive: true,
        processing: true,
        serverSide: true,
        ajax: {
            url: "/data_get_data/",
            type: 'POST',
            async: true,
            data: {
                "domain": domain,
                "model": "vervar",
                "id_var": id_vervar,
                "csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val()
            },
            dataSrc: function (json) {
                if (json.data === "no_data") {
                    // Tampilkan pesan jika data kosong
                    alert("Data tidak tersedia");
                    return [];
                } else {
                    return json.data;
                }
            }
        },
        "columns": [
            {
                "data": "vervar"
            },

            {
                "data": "kode_ver_id",
                "render": function (data, type, row, meta) {
                    return '<a href="#">' + data + '</a>';
                }
            },

        ],

    })


}
