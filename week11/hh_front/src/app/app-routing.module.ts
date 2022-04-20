import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CompanyComponent} from './company/company.component';
import { VacancyComponent } from './vacancy/vacancy.component';

const routes: Routes = [
  {path: 'companies', component: CompanyComponent},
  {path: 'companies/:id', component: VacancyComponent}
  /*{path: "albums/:id", component: AlbumDetailComponent},*/
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
