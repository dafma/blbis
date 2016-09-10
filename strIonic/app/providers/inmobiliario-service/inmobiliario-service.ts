import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

/*
  Generated class for the InmobiliarioService provider.

  See https://angular.io/docs/ts/latest/guide/dependency-injection.html
  for more info on providers and Angular 2 DI.
*/
@Injectable()
export class InmobiliarioService {
  data: any;

  constructor(private http: Http) {
    this.data = null;
  }
  load() {
    if ( this.data) {
      return Promise.resolve(this.data);
    }
    return new Promise(resolve => {
      this.http.get('http://127.0.0.1:8000/api/inmobiliario/')
      .map(res => res.json())
      .subscribe(data => {
        this.data = data;
        resolve(this.data);
      });
    });
  }

}

