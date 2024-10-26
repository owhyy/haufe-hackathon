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
	    <h1>Things</h1>
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
