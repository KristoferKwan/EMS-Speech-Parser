import React from 'react';
import { HashRouter, Route, hashHistory } from 'react-router-dom';
import EMS from './components/EMS';
// import more components
export default (
    <HashRouter history={hashHistory}>
     <div>
      <Route path='/' component={EMS} />
     </div>
    </HashRouter>
);