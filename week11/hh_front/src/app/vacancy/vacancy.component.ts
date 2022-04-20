import { Component, OnInit } from '@angular/core';
import {Vacancy} from '../models';
import {CompanyService} from '../company.service';
import {ActivatedRoute} from '@angular/router';
 
@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit {

  vacancies: Vacancy[] = [];

  constructor(
    private companyService: CompanyService,
    private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies() {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.companyService.getVacancies(id).subscribe((data) => {
         this.vacancies = data;
      });
    });
  }

}
