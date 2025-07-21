import { LoadingOutlined, PlusOutlined } from "@ant-design/icons";
import { Flex, message, Upload, Button } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import { useState } from "react";

const Query = () => {
  const [file, setFile] = useState(null);
  const uploadProps = {
    name: "file",
    action: "https://660d2bd96ddfa2943b33731c.mockapi.io/api/upload",
    headers: {
      authorization: "authorization-text",
    },
    onChange(info) {
      if (info.file.status !== "uploading") {
        console.log(info.file, info.fileList);
      }
      console.log(info, "info");
      if (info.file.status === "done") {
        setFile(info.file);
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === "error") {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };

  // const uploadPdf = async () => {
  //   try {
  //     const formData = new FormData();
  //     formData.append("file", file);
  //     // Change this URL to your Flask endpoint
  //     const response = await axios.post(
  //       "http://localhost:5000/upload-pdf",
  //       formData,
  //       {
  //         headers: {
  //           "Content-Type": "multipart/form-data",
  //         },
  //       }
  //     );
  //     onSuccess(response.data); // let Upload know it's done
  //   } catch (err) {
  //     onError(err);
  //   }
  // };

  return (
    <div>
      <Upload {...uploadProps}>
        <Button icon={<UploadOutlined />}>Click to Upload</Button>
      </Upload>
      {/* <Button onChange={uploadPdf}>Upload</Button>{" "} */}
    </div>
  );
};

export default Query;
