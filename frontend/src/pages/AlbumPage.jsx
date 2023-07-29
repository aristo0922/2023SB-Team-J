/* eslint-disable react/no-array-index-key */
/* eslint-disable no-use-before-define */
/* eslint-disable func-names */
/* eslint-disable array-callback-return */
/* eslint-disable no-undef */
/* eslint-disable no-plusplus */
/* eslint-disable no-unused-vars */
/* eslint-disable no-shadow */
/* eslint-disable import/no-extraneous-dependencies */
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Masonry from 'react-masonry-css';
import axios from 'axios';
import styled from 'styled-components';
import { motion } from 'framer-motion';
// import UploadBtn from '../components/UploadBtn';
import Header from '../components/HeaderAlbum';
import AlbumDetailModal from '../components/AlbumDetailModal';
import PlusBtn from '../assets/images/plusBtn.png';
import Loading from '../components/Loading';
import FloatingImage from '../components/FloatingImage';

function AlbumPage() {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [resultImgId, setResultImgId] = useState('');

  const openModalHandler = (id) => {
    setResultImgId(id);
    setIsOpen(true);
  };

  const breakpointColumnObj = {
    default: 4, // 기본 레이아웃에서 4열
    1200: 3, // 창 너비 1200px 이하일 때 3열
    900: 2, // 창 너비 900px 이하일 때 2열
    600: 1, // 창 너비 600px 이하일 때 1열
  };
  const [images, setImages] = useState([]);

  async function inquireAlbum() {
    setIsLoading(true);

    try {
      const response = await axios.post('http://localhost:8000/api/v1/album/', {
        user_id: '1',
      });

      // 서버 응답 처리
      const albumData = response.data; // 응답 데이터
      console.log(albumData);
      // 이미지 배열에 추가

      setImages((prevImages) => [...prevImages, ...albumData]);

      setIsLoading(false);
    } catch (error) {
      console.log(error);
      console.log('에러 발생');
    } finally {
      setIsLoading(false);
    }
  }

  // 앨범 조회 요청 보내기
  useEffect(() => {
    // 요청을 1번만 보내게 설정
    inquireAlbum();
  }, []);

  return (
    <div>
      <Container>
        <Header />
        <MainWrap>
          <AddBtn
            onClick={() => navigate('/choose')}
            whileHover={{ scale: 1.2 }}
            whileTap={{ borderRadius: '50%' }}
          />
          <MyMasonryGrid
            breakpointCols={breakpointColumnObj}
            className="my-masonry-grid"
            columnClassName="my-masonry-grid_column"
          >
            {isLoading && (
              <LoadingWrap>
                <Loading />
              </LoadingWrap>
            )}
            {!isLoading &&
              images.length > 0 &&
              images.map((img, i) => {
                return (
                  <MyMasonryGridColumn key={img.result_image_id}>
                    <ImageWithShadow
                      src={img.result_url}
                      alt="photo"
                      onClick={() => openModalHandler(img.result_image_id)} // 보내는 값에 따라 다름
                    />
                    {/* id값을 모달창에 보내야됨 */}
                  </MyMasonryGridColumn>
                );
              })}
            {!isLoading && images.length === 0 && (
              <FloatingWrap>
                <FloatingImage />
              </FloatingWrap>
            )}

            {isOpen && (
              <AlbumDetailModal
                imgId={resultImgId}
                setIsOpen={setIsOpen}
                setImages={setImages} // 삭제된 이미지가 모달창을 닫은 후에 자동으로 렌더링되도록 수정하기 위해 images 상태를 업데이트하는 함수를 정의
              />
            )}
          </MyMasonryGrid>
          {/* <CenteredButton>
            <UploadBtn path="/upload" />
          </CenteredButton> */}
        </MainWrap>
      </Container>
    </div>
  );
}

export default AlbumPage;

const Container = styled.div`
  width: 100%;
  min-height: 100vh;
  background: ${(props) => props.theme.backgroundColor};
`;

const MainWrap = styled.div`
  max-width: 1440px;
  width: 76vw;
  height: 100%;
  margin: 0 auto;
  flex-shrink: 0;
  border: 3px solid black;
  background-color: white;
`;

const AddBtn = styled(motion.div)`
  position: absolute;
  top: 10vh;
  left: 0;
  right: 0;
  margin: 0 auto;
  width: 60px; // width 추가
  height: 60px; // height 추가
  background: url(${PlusBtn}) no-repeat center/cover;

  &:hover {
    cursor: pointer;
  }
`;
const MyMasonryGrid = styled(Masonry)`
  display: flex;
  margin-top: 30vh;
  margin-left: -30px; /* 컬럼 간격을 조절하기 위해 음수 마진을 적용 */
  width: auto;

  &::after {
    content: '';
    display: block;
    clear: both;
  }
`;

const MyMasonryGridColumn = styled.div`
  padding-left: 30px; /* 컬럼 간격을 조절하기 위해 패딩을 적용 */
  background-clip: padding-box;

  img {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
`;

const ImageWithShadow = styled.img`
  box-shadow: 10px 10px 6px 0px rgba(0, 0, 0, 0.25);
`;

const LoadingWrap = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
`;

const FloatingWrap = styled.div`
  justify-content: center;
  align-items: center;
  padding-left: 39rem;
`;
