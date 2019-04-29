$(document).ready(function () {

    $('#edit').click(function () {
        var ids = [];

        $("input:checkbox[name=todo]:checked").each(function () {
            ids.push($(this).val());
        });
        
        if (ids.length == 1) {
            window.location = "/todo/edit-todo/" + ids[0] + "/"
        }

        if (ids.length != 1) {
            toastr.warning('To edit, please select only ONE or at lease ONE to-do.');
        }
    });

    $('#delete').click(function () {
        
        var ids = [];

        $("input:checkbox[name=todo]:checked").each(function () {
            ids.push($(this).val());
        });
        
        if (ids.length == 1) {
            window.location = "/todo/delete-todo/" + ids[0] + "/"
        }

        if (ids.length != 1) {
            toastr.warning('To delete, please select only ONE or at lease ONE to-do.');
        }
    });
})