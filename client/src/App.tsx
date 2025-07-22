import { BrowserRouter, Route, Routes } from "react-router";
import Query from "./pages/Query";
import UploadPdf from "./pages/UploadPdf";
import React from "react";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Query />} />
        <Route path="/upload" element={<UploadPdf />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
