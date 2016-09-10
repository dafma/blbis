import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {InmobiliarioService} from '../../providers/inmobiliario-service/inmobiliario-service';

@Component({
  templateUrl: 'build/pages/page1/page1.html',
  providers: [InmobiliarioService]
})
export class Page1 {
  prod: any[] = [];

  constructor(
    public navCtrl: NavController,
    private inmobiliarioService: InmobiliarioService) {

    this.inmobiliarioService.load()
    .then(data => {
      this.prod = data;
      console.log(this.prod);
      
    }) ;  
  }
}
