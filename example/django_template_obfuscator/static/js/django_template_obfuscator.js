text_to_deobfuscate = document.getElementById('obfuscated').innerHTML;

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

converted = rot13(text_to_deobfuscate);

document.getElementById('obfuscated').innerHTML = converted;
