export class PromptListComponent {

  prompts:any

  constructor(private service:PromptService){}

  ngOnInit(){
    this.service.getPrompts().subscribe(data=>{
      this.prompts=data
    })
  }

}

<h2>Prompt Library</h2>

<div *ngFor="let p of prompts">
  <a [routerLink]="['/prompts',p.id]">
    {{p.title}} (Complexity: {{p.complexity}})
  </a>
</div>