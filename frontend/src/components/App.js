import './App.css';
import styled from 'styled-components';
import SignUpModal from './components/SignUpModal';
import LoginModal from './components/LoginModal';
import AlbumModal from './components/AlbumModal';
import { useState } from 'react';

function App() {
  const [loginModalOpen, setLoginModalOpen] = useState(false);
  const [signUpModalOpen, setSignUpModalOpen] = useState(false);
  const [albumModalOpen, setAlbumModalOpen] = useState(false);
  const handleOpenLoginModal = () => {
    setLoginModalOpen(true);
  };
  const handleCloseLoginModal = () => {
    setLoginModalOpen(false);
  };
  const handleOpenSignUpModal = () => {
    setSignUpModalOpen(true);
  };
  const handleCloseSignUpModal = () => {
    setSignUpModalOpen(false);
  };

  const handleOpenAlbumModal = () => {
    setAlbumModalOpen(true);
  };
  const handleCloseAlbumModal = () => {
    setAlbumModalOpen(false);
  };

  return (
    <>
      <LoginBtn onClick={handleOpenLoginModal}>로그인</LoginBtn>
      <SignUpBtn onClick={handleOpenSignUpModal}>회원가입</SignUpBtn>
      {
        <SignUpModal
          isOpen={signUpModalOpen}
          onClose={handleCloseSignUpModal}
        />
      }
      {<LoginModal isOpen={loginModalOpen} onClose={handleCloseLoginModal} />}
      <AlbumImageBtn onClick={handleOpenAlbumModal}>앨범이미지</AlbumImageBtn>
      {
        <AlbumModal
          isOpen={albumModalOpen}
          onClose={handleCloseAlbumModal}
        ></AlbumModal>
      }
    </>
  );
}

export default App;

const SignUpBtn = styled.button`
  width: 93px;
  height: 35px;
  border: 1px solid black;
  border-radius: 30px;
  padding: 0;
  font-size: 16px;

  &:hover {
    cursor: pointer;
  }
`;

const LoginBtn = styled.button`
  width: 93px;
  height: 35px;
  border: 1px solid black;
  border-radius: 30px;
  padding: 0;
  font-size: 16px;

  &:hover {
    cursor: pointer;
  }
`;

const AlbumImageBtn = styled.button`
  width: 93px;
  height: 35px;
  border: 1px solid black;
  border-radius: 30px;
  padding: 0;
  font-size: 16px;

  &:hover {
    cursor: pointer;
  }
`;
