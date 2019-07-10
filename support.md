# SpinW Support

If you are having problems with SpinW you can contact support by the webform or *support AT spinw DOT org*. This can get busy, so apologies for delays.

If you have found a bug, documentation error or have a suggestion please use the [github issue tracker](https://github.com/SpinW/spinw/issues)

<form action="https://mailthis.to/spinw_sup" method="POST" encType="multipart/form-data">
    <!-- Name -->
    <input type="text" name="name" placeholder="Your name" required>
    <!-- Email -->
          <input type="email" name="email" placeholder="you@mail.com" required>
          <!-- Issue title -->
          <input type="text" name="_subject" placeholder="Subject" required>
          <!-- Textarea (Message) -->
          <textarea name="message" placeholder="Message" required></textarea>
          <!-- File attachments -->
          <label id="button-for-upload-file" for="upload-file">Upload file...</label>
          <input id="upload-file" type="file" name="file" placeholder="">
          <!-- Optional (hidden) fields -->
          <!-- Custom email Subject -->
          <!-- <input type="hidden" name="_subject" value="Contact form submitted"> -->
          <!-- Custom email ReplyTo Address -->
          <!-- <input type="hidden" name="_replyto" value="foo@bar.co">  -->
          <!-- Honeypot (to catch comment spam bots) -->
          <input type="hidden" name="_honeypot" value="">
          <!-- Apply a custom confirmation message on the second step -->
          <!-- <input type="hidden" name="_confirmation" value="custom confirmation message!!!"> -->
          <!-- Redirect to a page after recaptcha -->
          <!-- <input type="hidden" name="_after" value="https://easydiffraction.github.io/thankyou.html"> -->
          <!-- Submit Button -->
          <input type="submit" name="submit" value="Submit Form" class="button">
</form>