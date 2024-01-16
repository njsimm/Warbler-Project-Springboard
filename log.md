# Log to track changes/updates

1. **File:** `log.md`
   - Created `log.md`
2. **File:** `app.py`

   - Completed "Step Two: Fix Logout"
   - Updated Code:

     ```python
     @app.route('/logout')
     def logout():
        """
        Handle logout of user.
        - The current method to logout uses a GET request; however, future iterations should use a POST request as it is more secure.
        """

        user = g.user
        do_logout()
        flash(f"Goodbye {user.username}! See you next time!", "success")

        return redirect('/login')
     ```

3. **File:** `detail.html`
   - Completed "Step Three: Fix User Profile" (location, bio, and header image)
   - Updated Code:
     ```html
     <div class="col-sm-3">
       <h4 id="sidebar-username">@{{ user.username }}</h4>
       <p>{{ user.bio }}</p>
       <p class="user-location">
         <span class="fa fa-map-marker">{{ user.location }}</span>
       </p>
     </div>
     ```
     ```html
     <div id="warbler-hero" class="full-width">
       <img
         src="{{ user.header_image_url }}"
         alt="Header image for {{ user.username }}"
       />
     </div>
     ```
4. **Files:** `followers.html`, `following.html`, `index.html`

   - Completed "Step Four: Fix User Cards"
   - Updated Code for `followers.html`:

     ```html
     <p class="card-bio">{{ follower.bio }}</p>
     ```

   - Updated Code for `following.html`:
     ```html
     <p class="card-bio">{{ followed_user.bio }}</p>
     ```
   - Updated Code for `index.html`:
     ```html
     <p class="card-bio">{{ user.bio }}</p>
     ```

5. **Files:** `app.py` and `forms.py`

   - Completed "Step Five: Profile Edit"
   - Updated Code for `app.py`:

     ```python
     @app.route('/users/profile', methods=["GET", "POST"])
     def profile():
       """Update profile for current user."""

       if not g.user:
           flash("Access unauthorized.", "danger")
           return redirect("/")

       user = g.user
       form = UserProfileEditForm(obj=user)

       if form.validate_on_submit():
           if not User.authenticate(user.username, form.password.data):
               flash("Password is incorrect.", 'danger')
               return redirect("/")

           user.username = form.username.data
           user.email = form.email.data
           user.image_url = form.image_url.data
           user.header_image_url = form.header_image_url.data
           user.bio = form.bio.data

           db.session.commit()

           return redirect(f'/users/{user.id}')

       return render_template('/users/edit.html', form=form, user=user)
     ```

   - Updated Code for `forms.py`:

     ```python
     class UserProfileEditForm(FlaskForm):
         """Form for editing user profile"""

         username = StringField('Username')
         email = StringField('E-mail', validators=[Email()])
         image_url = StringField('Image URL')
         header_image_url = StringField('Header Image URL')
         bio = StringField('Bio')
         password = PasswordField('Password', validators=[DataRequired()])
     ```

6. **Files:** `app.py`

- Completed "Step Six: Fix Homepage"
- Updated Code for `app.py`:

  ```python
  @app.route('/')
  def homepage():
      """Show homepage:

      - anon users: no messages
      - logged in: 100 most recent messages of followed_users
      """

      if g.user:
          all_messages = (Message.query.order_by(Message.timestamp.desc()).all())

          messages_of_followed_users = [message for message in all_messages if message.user in g.user.following]

          messages = messages_of_followed_users[:100]

          return render_template('home.html', messages=messages)

      else:
          return render_template('home-anon.html')
  ```

7. **Files:** `app.py`, `detail.html`, `home.html` `likes.html`

- Completed "Part Two: Add Likes"
- Updated Code for `app.py`:

  ```python
  @app.route('/users/toggle_like/<int:message_id>', methods=["POST"])
  def message_like(message_id):
      """Like a message."""

      if not g.user:
          flash("Access unauthorized.", "danger")
          return redirect("/")

      user=g.user
      msg = Message.query.get_or_404(message_id)

      if msg.user_id != user.id:
          if msg not in user.likes:
              user.likes.append(msg)
              db.session.commit()
          else:
              user.likes.remove(msg)
              db.session.commit()

      return redirect(f"/messages/{user.id}/likes")

  @app.route('/messages/<int:user_id>/likes')
  def messages_liked_by_user(user_id):
      """Shows messages liked by signed in user"""

      if not g.user:
          flash("Access unauthorized.", "danger")
          return redirect("/")

      user = User.query.get_or_404(user_id)
      liked_messages = user.likes

      return render_template('messages/likes.html', user=user, messages=liked_messages)
  ```

- Updated Code for `detail.html`:
  ```html
  <h4>
    <a href="/messages/{{ user.id }}/likes">{{ user.likes | length }}</a>
  </h4>
  ```
- Updated Code for `home.html`:

  ```html
  {% for msg in messages %} {% if msg not in g.user.likes %}
  <li class="list-group-item">
    <a href="/messages/{{ msg.id  }}" class="message-link" />
    <a href="/users/{{ msg.user.id }}">
      <img src="{{ msg.user.image_url }}" alt="" class="timeline-image" />
    </a>
    <div class="message-area">
      <a href="/users/{{ msg.user.id }}">@{{ msg.user.username }}</a>
      <span class="text-muted">{{ msg.timestamp.strftime('%d %B %Y') }}</span>
      <p>{{ msg.text }}</p>
    </div>
    <form
      method="POST"
      action="/users/toggle_like/{{ msg.id }}"
      id="messages-form"
    >
      <button
        class="
                btn 
                btn-sm 
                {{'btn-primary' if msg.id in likes else 'btn-secondary'}}"
      >
        <i class="fa fa-thumbs-up"></i>
      </button>
    </form>
  </li>
  {% else %}
  <li class="list-group-item">
    <a href="/messages/{{ msg.id  }}" class="message-link" />
    <a href="/users/{{ msg.user.id }}">
      <img src="{{ msg.user.image_url }}" alt="" class="timeline-image" />
    </a>
    <div class="message-area">
      <a href="/users/{{ msg.user.id }}">@{{ msg.user.username }}</a>
      <span class="text-muted">{{ msg.timestamp.strftime('%d %B %Y') }}</span>
      <p>{{ msg.text }}</p>
    </div>
    <form
      method="POST"
      action="/users/toggle_like/{{ msg.id }}"
      id="messages-form"
    >
      <button
        class="
                btn 
                btn-sm 
                {{'btn-primary' if msg.id in likes else 'btn-secondary'}}"
      >
        <i class="fa fa-star"></i>
      </button>
    </form>
  </li>
  {% endif %} {% endfor %}
  ```

- Created `likes.html` in order for a signed in user to view their liked messages.
