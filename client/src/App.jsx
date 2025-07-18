import { BrowserRouter, Route, Routes } from "react-router";
import Query from "./pages/Query";
import UploadPdf from "./pages/UploadPdf";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Query />} />
        <Route page="/upload" element={<UploadPdf />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
