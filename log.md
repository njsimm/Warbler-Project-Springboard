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
