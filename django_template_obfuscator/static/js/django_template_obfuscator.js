deobfuscate_elements = document.getElementsByClassName('obfuscated');

function rot13(str) {
  var input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  var output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm';
  var index = x => input.indexOf(x);
  var translate = x => (index(x) > -1 ? output[index(x)] : x);
  return str
    .split('')
    .map(translate)
    .join('');
}

Array.prototype.forEach.call(deobfuscate_elements, function(element) {
  converted = rot13(element.innerHTML);
  element.innerHTML = converted;
});
