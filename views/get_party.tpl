%rebase ('head.tpl')
<main class="container" style="text-align: center;">
   <article>
      <h1> {{party.name}} </h1>
      <p>
      <i>Code: <mark>{{party.code}}</mark></i>
      </p>
      Budget progress
      </br>
      <progress value="{{party.current_budget}}" max="{{party.max_budget}}" style="max-width: 50%;"></progress>
      <p>
         {{party.current_budget}}/{{party.max_budget}}
      </p>
      <ul>
         <article style="text-align: left;">
	 <div style="display: flex; align-items: center; justify-content: space-between;">
	    <h1>Things</h1>
	    <a href="#" style="color: inherit; text-decoration: none;"> <!-- Wrapping in <a> to make clickable -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
            <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM11 11H7V13H11V17H13V13H17V11H13V7H11V11Z"></path>
        </svg>
    </a>
         </div>
	    <hr/>
            % for thing in party.things:
            <li style="list-style-type: none;">
               <span style="display: inline-block; width: 100%;">
                  <p>
                     <h4>{{thing.name}}</h4>
                  </p>
                  <p>
                     <mark>{{thing.price}} RON</mark>
                  </p>
                  <span id="user-dropdown" style="float: right;">
  		    <select hx-target="this" hx-patch="party/{{party.id}}/reassign/{{thing.id}}" hx-include="[name='responsible']" hx-trigger="change" name="responsible" class="dropdown">

		    <option selected value="{{thing.responsible.id}}">{{thing.responsible.username}}</option>
		       % for user in filter(lambda u: u.id != thing.responsible.id, party.users):
		       	    <option value="{{user.id}}">{{user.username}}</option>
   		       % end
		    </select>		    
                  </span>
                  <i>{{thing.description}}</i>
               </span>
            </li>
            % end
         </article>
      </ul>
   </article>
</main>
