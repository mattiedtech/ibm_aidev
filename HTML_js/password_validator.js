const passwords = ["Password123", "buttz", "ValidAF69", "much_too_long_for_this","12345"];

function validatePasswords(passwords) {
  const regex = /^[a-zA-Z0-9]{8,20}$/;
  for (let i = 0; i < passwords.length; i++) {
    if (regex.test(passwords[i])) {
      console.log(`${passwords[i]} is valid.`)
    } else {
      console.log(`${passwords[i]} is invalid.`)
    }
  }
}

validatePasswords(passwords);
