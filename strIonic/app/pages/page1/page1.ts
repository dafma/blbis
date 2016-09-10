import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import {InmobiliarioService} from '../../providers/inmobiliario-service/inmobiliario-service';
import {ItemDetailPage} from '../item-detail/item-detail';


@Component({
  templateUrl: 'build/pages/page1/page1.html',
  providers: [InmobiliarioService]
})
export class Page1 {
  prod: any[] = [];
  selectedItem: any;

  constructor(
    public navCtrl: NavController,
    private inmobiliarioService: InmobiliarioService,
    private navParams: NavParams) {

   this.selectedItem = navParams.get('pro');   

    this.inmobiliarioService.load()
    .then(data => {
      this.prod = data;
      console.log(this.prod);
      
    }) ;  
  }
    itemTapped(event, pro) {
    this.navCtrl.push(ItemDetailPage, {
      pro: pro
    });
}
}
