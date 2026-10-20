// PWA
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register(new URL('manifest.webmanifest', document.baseURI).pathname.replace('manifest.webmanifest','') + 'sw.js').catch(function(){});
  });
}
// Contact form -> mailto
var qf = document.getElementById('qform');
if (qf) {
  qf.addEventListener('submit', function (e) {
    e.preventDefault();
    var n = qf.name.value.trim(), p = qf.phone.value.trim(), m = qf.msg.value.trim();
    var s = encodeURIComponent('Project enquiry from ' + n);
    var b = encodeURIComponent('Name: ' + n + '\nPhone: ' + p + '\n\n' + m);
    window.location.href = 'mailto:info@blueivygroup.in?subject=' + s + '&body=' + b;
  });
}
