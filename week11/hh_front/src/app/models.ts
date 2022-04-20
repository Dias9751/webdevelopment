export interface Company{
  id: number;
  name: string;
}
  
export interface AuthToken {
  token: string;
}

export interface Vacancy{
  id: number;
  name: string;
  description: string;
  salary: number;
}