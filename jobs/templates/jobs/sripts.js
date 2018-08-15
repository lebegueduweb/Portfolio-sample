<script>
var inNewWindow = OpenInNewWindow()

function OpenInNewWindow() {
    var w = window.open();
    w.document.open();
    w.document.write("<h2></h2>");
    w.document.close();
}
</script>