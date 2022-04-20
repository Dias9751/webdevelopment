import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {AuthToken, Company, Vacancy} from './models';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  BASE_URl = 'http://127.0.0.1:8000';/*'http://localhost:8000';*/

  constructor(private http: HttpClient) {
  }
 
  login(username: string, password: string): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.BASE_URl}/hh_back/login/`, {
      username,
      password
    });
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URl}/hh_back/companies/`);
  }

  getVacancies(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URl}/hh_back/companies/${id}/vacancies/`);
  }
}